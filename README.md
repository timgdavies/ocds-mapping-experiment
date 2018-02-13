## OCDS Mapper

This repository contains an experiment to see how we can use the Open Contracting Data Standard schema to generate an interface for:

* An improved tool for mapping between existing data systems and OCDS;
* Creating use-case mappings, that describe particular required fields;
* Generating annotation documents that can be used to describe the way in which fields within a published OCDS document should be interpreted. 

The current implementation makes use of Jeremy Dorn's [json-editor](https://github.com/jdorn/json-editor) and:

* Reads a version of the OCDS schema with added `propertyOrder` values (provided by running `add-property-order.py`);
* Resolves all references; 
* Replaces *most* leaf values in the tree structure with a mapping object (defined in mapping.json) that can be used to record mappings;
* Cleans up a few other issues that break schema display (e.g. null values in enums); 
* Performs some basic formatting of the display.

The resulting JSON mapping can be accessed from the JSON button at the top of the screen. 

## How could this be used?

Mapping already forms part of the OCDS implementation process. However, it may be possible to also use mapping documents as part of the *interpretation* and display of OCDS data. 

A `mapping` or `annotation` document could become part of the meta-data of any OCDS release. For example, a release might contain:

```json
{
    "meta":{
        "mappingDocument":"http://mapping.open-contracting.org/gb/ccs-map.json",
        "annotationDocuments":["http://notes.open-contracting.org/gb/ccs-annotate.json"]
    },
    "tender":{
        "value":{
            "amount":1000,
            "currency":"GBP"
        }
    }
}
```

And then `ccs-map.json` would contain:

```json
{
  "tender": {
    "value": {
      "amount": [
        {
          "mapsTo": "contracts_finder.tender_estimated_value",
          "mappingNote": "If in foreign currency, converted to GBP at exchange rate as of release date."
        }
      ]
    }
  }
}
```

And `ccs-annotate.json` would contain something like:

```json
{
  "tender": {
    "value": {
      "amount": [
        {
          "annotation": "The law requires an estimate value to be provided at the time a contacting process is approved. This value may be updated at a future point following process XYZ."
        }
      ]
    }
  }
}
```

A tool reading the data can choose to use the contents of the `mapping` and `annotation` files to display within a user interface.

Viewing the mapping or annotation files from a range of organisations side-by-side can be used to see if data is being consistently mapped. 

## Next steps

* Support mapping at the object level;
* Continued work on schema transformation, layout and interface;
* Allow users to specify an existing list of source data fields and example data to map to;

## Future features 

* Build and validate an example release based on the mapping provided;
* Allow users to select an extensions from the extension directory, and update the mapping to include these;
* Provide features for saving, exporting and reporting on mappings. 

